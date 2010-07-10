# rubygem-rails polisher registration

project :name => 'rubygem-rails' do |rails|
  rails.add_gem :name => "rails", :uri => 'http://rubygems.org/gems/rails-%{version}.gem', :primary_source => true

  rails.version "*", :depends_on => project(:name => 'ruby')
  
  rails.on_version "*",           "download sources"

  rails.on_version "=", "2.3.8", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @stable_mock_env
  rails.on_version "=", "2.3.8", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  rails.on_version ">=", "2.3.8", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @maintenance_mock_env
  rails.on_version ">=", "2.3.8", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  # uncomment when rails is supportend on ruby 1.9
  #rails.on_version ">=", "3.0.0", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @devel_mock_env
  #rails.on_version ">=", "3.0.0", "update yum repo", :repo => "#{artifacts_dir}/repos/devel"

  rails.on_version "*",           "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
end
