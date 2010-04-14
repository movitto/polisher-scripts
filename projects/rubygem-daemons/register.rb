# rubygem-daemons polisher registration

project :name => 'rubygem-daemons' do |daemons_project|
  daemons_project.add_gem :name => 'daemons', :uri => 'http://rubygems.org/gems/daemons-%{version}.gem', :primary_source => true

  daemons_project.on_version "*", "create rpm package", "#{@project_dir}/template.spec"
  daemons_project.on_version "*", "update yum repo", "#{@artifacts_dir}/repos/rawhide"
  daemons_project.on_version "*", "update yum repo", "#{@artifacts_dir}/repos/stable"
  daemons_project.on_version "*", "update yum repo", "#{@artifacts_dir}/repos/maintenance"
  daemons_project.on_version "*", "update yum repo", "#{@artifacts_dir}/repos/devel"
end
