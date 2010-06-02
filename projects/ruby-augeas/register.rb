# ruby-augeas polisher registration

project :name => 'ruby-augeas' do |augeas|
  augeas.add_archive :name => 'ruby-augeas', :uri => 'http://augeas.net/download/ruby/ruby-augeas-%{version}.tgz', :primary_source => true
  augeas.add_patch   :name => 'ruby19-augeas-fix', :uri => "#{@morsiorg_polisher_sources}/augeas-ruby-1.9-fix.patch"  # my fix to make augeas 1.9 compatible

  augeas.version "*", :depends_on => project(:name => 'ruby')

  augeas.on_version "*",           "download sources"

  augeas.on_version "=",  "0.3.0", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @stable_mock_env
  augeas.on_version "=",  "0.3.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  # TODO uncomment when ruby 1.8.7 is setup in maintenance repo
  #augeas.on_version ">=", "0.3.0", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @maintenance_mock_env
  #augeas.on_version ">=", "0.3.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  augeas.on_version ">=", "0.3.0", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @devel_mock_env
  augeas.on_version ">=", "0.3.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"

  augeas.on_version "*",           "update yum repo",     :repo =>"#{@artifacts_dir}/repos/rawhide"
end
