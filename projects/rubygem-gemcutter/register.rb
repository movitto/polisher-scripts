# rubygem-gemcutter polisher registration

project :name => 'rubygem-gemcutter' do |gc|
  gc.add_gem :name => "gemcutter", :uri => 'http://rubygems.org/gems/gemcutter-%{version}.gem', :primary_source => true
  
  gc.version "*", :depends_on => project(:name => 'ruby')

  gc.on_version "*",           "download sources"

  gc.on_version "=",  "0.3.0", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @stable_mock_env
  gc.on_version "=",  "0.3.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  # TODO uncomment when ruby 1.8.7 is setup in maintenance repo
  # gc.on_version ">",  "0.3.0", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @maintenance_mock_env
  # gc.on_version ">", "0.3.0",  "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  gc.on_version ">",  "0.3.0", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @devel_mock_env
  gc.on_version ">",  "0.3.0",  "update yum repo",   :repo => "#{@artifacts_dir}/repos/devel"

  gc.on_version "*",           "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
end
