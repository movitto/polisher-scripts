# rubygem-rake polisher registration

project :name => 'rubygem-rake' do |rake|
  rake.add_gem :name => 'rake', :uri => 'http://rubygems.org/gems/rake-%{version}.gem', :primary_source => true

  rake.on_version "*",          "download sources"
  rake.on_version "*",          "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @system_mock_env
  rake.on_version "*",          "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
  rake.on_version "=", "0.8.7", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable"
  rake.on_version "=", "0.8.7", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance"
  rake.on_version "*",          "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"
end
