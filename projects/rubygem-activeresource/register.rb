# rubygem-activeresource polisher registration

project :name => 'rubygem-activeresource' do |activeresource|
  activeresource.add_gem :name => 'activeresource', :uri => 'http://rubygems.org/downloads/activeresource-%{version}.gem', :primary_source => true

  activeresource.on_version "*",           "download sources"

  activeresource.on_version "=",  "2.3.8", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @stable_mock_env
  activeresource.on_version "=",  "2.3.8", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  activeresource.on_version ">=", "2.3.8", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @maintenance_mock_env
  activeresource.on_version ">=", "2.3.8", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  # uncomment when Ruby 1.9 supports rails 3
  #activeresource.on_version "=",  "3.0.0", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @devel_mock_env
  #activeresource.on_version ">=", "3.0.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"

  activeresource.on_version "*",           "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
end
