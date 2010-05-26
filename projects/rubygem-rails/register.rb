# rubygem-rails polisher registration

project :name => 'rubygem-rails' do |rails|
  rails.add_gem :name => "rails", :uri => 'http://rubygems.org/gems/rails-%{version}.gem', :primary_source => true
  
  rails.on_version "*",           "download sources"
  rails.on_version "*",           "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @system_mock_env
  rails.on_version "*",           "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
  rails.on_version "=",  "2.3.5", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable"
  rails.on_version ">=", "3.0.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance"
  #rails.on_version ">=", "3.0.0", "update yum repo", "devel" # uncomment when rails is supportend on ruby 1.9
end
