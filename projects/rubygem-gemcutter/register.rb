# rubygem-gemcutter polisher registration

project :name => 'rubygem-gemcutter' do |gc|
  gc.add_gem :name => "gemcutter", :uri => 'http://rubygems.org/gems/gemcutter-%{version}.gem', :primary_source => true
  
  gc.on_version "*",           "download sources"
  gc.on_version "*",           "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @system_mock_env
  gc.on_version "*",           "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
  gc.on_version "=",  "0.3.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable"
  gc.on_version ">", "0.3.0",  "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance"
  gc.on_version ">", "0.3.0",  "update yum repo",        :repo => "devel"
end
