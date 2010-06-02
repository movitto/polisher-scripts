# rubygem-activerecord polisher registration

# should be named rubygem-activerecord but isn't currently in Fedora

project :name => 'ruby-activerecord' do |activerecord|
  activerecord.add_gem :name => 'activerecord', :uri => 'http://rubygems.org/downloads/activerecord-%{version}.gem', :primary_source => true

  activerecord.on_version "*",           "download sources"

  activerecord.on_version "=",  "2.0.1", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @stable_mock_env
  activerecord.on_version "=",  "2.0.1", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  # TODO uncomment when ruby 1.8.7 is setup in maintenance repo
  #activerecord.on_version "=",  "2.3.5", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @maintenance_mock_env
  #activerecord.on_version "=",  "2.3.5", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  activerecord.on_version "=",  "3.0.0", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @devel_mock_env
  activerecord.on_version ">=", "3.0.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"

  activerecord.on_version "*",           "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
end
