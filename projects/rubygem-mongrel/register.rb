# rubygem-mongrel polisher registration

project :name => 'rubygem-mongrel' do |mongrel|
  mongrel.add_gem :name => 'mongrel',   :uri => 'http://rubygems.org/gems/mongrel-%{version}.gem', :primary_source => true
  mongrel.add_gem :name => 'multipart', :uri => 'http://gems.rubyforge.org/gems/cgi_multipart_eof_fix-2.5.0.gem'

  mongrel.version "*", :depends_on => project(:name => 'ruby')

  mongrel.on_version "*",           "download sources"

  mongrel.on_version "=",  "1.1.5", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @stable_mock_env
  mongrel.on_version "=",  "1.1.5", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  # TODO uncomment when ruby 1.8.7 is setup in maintenance repo
  #mongrel.on_version ">=", "1.2.0", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @maintenance_mock_env
  #mongrel.on_version ">=", "1.2.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  mongrel.on_version ">=", "1.2.0", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @devel_mock_env
  mongrel.on_version ">=", "1.2.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"

  mongrel.on_version "*",           "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
end
