# rubygem-activesupport polisher registration

project :name => 'rubygem-activesupport' do |activesupport|
  activesupport.add_gem :name => 'activesupport', :uri => 'http://rubygems.org/downloads/activesupport-%{version}.gem', :primary_source => true

  activesupport.on_version "*",           "download sources"

  activesupport.on_version "=",  "2.3.8", "create rpm package", :spec => "#{@project_dir}/template-2.3.5.spec", :mock => @stable_mock_env
  activesupport.on_version "=",  "2.3.8", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  activesupport.on_version "=",  "2.3.8", "create rpm package", :spec => "#{@project_dir}/template-2.3.5.spec", :mock => @maintenance_mock_env
  activesupport.on_version "=",  "2.3.8", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  activesupport.on_version ">=", "3.0.0", "create rpm package", :spec => "#{@project_dir}/template-3.0.0.spec", :mock => @maintenance_mock_env
  activesupport.on_version ">=", "3.0.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  # uncomment when Ruby 1.9 supports rails 3
  #activesupport.on_version "=",  "3.0.0", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @devel_mock_env
  #activesupport.on_version ">=", "3.0.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"

  activesupport.on_version "*",           "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
end
