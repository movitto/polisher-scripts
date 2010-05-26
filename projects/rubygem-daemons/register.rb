# rubygem-daemons polisher registration

project :name => 'rubygem-daemons' do |daemons|
  daemons.add_gem :name => 'daemons', :uri => 'http://rubygems.org/gems/daemons-%{version}.gem', :primary_source => true

  daemons.on_version "*", "download sources"
  daemons.on_version "*", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @system_mock_env
  daemons.on_version "*", "update yum repo", :repo => "#{@artifacts_dir}/repos/rawhide"
  daemons.on_version "*", "update yum repo", :repo => "#{@artifacts_dir}/repos/stable"
  daemons.on_version "*", "update yum repo", :repo => "#{@artifacts_dir}/repos/maintenance"
  daemons.on_version "*", "update yum repo", :repo => "#{@artifacts_dir}/repos/devel"
end
