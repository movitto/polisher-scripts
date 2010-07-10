# rubygem-actionmailer polisher registration

project :name => 'rubygem-actionmailer' do |actionmailer|
  actionmailer.add_gem :name => 'actionmailer', :uri => 'http://rubygems.org/downloads/actionmailer-%{version}.gem', :primary_source => true

  actionmailer.on_version "*",           "download sources"

  actionmailer.on_version "=",  "2.3.8", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @stable_mock_env
  actionmailer.on_version "=",  "2.3.8", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  actionmailer.on_version ">=", "2.3.8", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @maintenance_mock_env
  actionmailer.on_version ">=", "2.3.8", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  # uncomment when Ruby 1.9 supports rails 3
  #actionmailer.on_version "=",  "3.0.0", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @devel_mock_env
  #actionmailer.on_version ">=", "3.0.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"

  actionmailer.on_version "*",           "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
end
