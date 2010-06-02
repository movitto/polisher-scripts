# rubygem-rake polisher registration

project :name => 'rubygem-rake' do |rake|
  rake.add_gem :name => 'rake', :uri => 'http://rubygems.org/gems/rake-%{version}.gem', :primary_source => true

  rake.version "*", :depends_on => project(:name => 'ruby')

  # starting in ruby 1.9 rake is included as part of
  # the official ruby project proper. still provide package for
  # the devel repo, but it will be empty / pull in ruby

  rake.on_version "*",          "download sources"


  rake.on_version "=",  "0.8.7", "create rpm package", :spec => "#{@project_dir}/template-1.8.spec", :mock => @stable_mock_env
  rake.on_version "=",  "0.8.7", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  # TODO uncomment when ruby 1.8.7 is setup in maintenance repo
  #rake.on_version "=",  "0.8.7", "create rpm package", :spec => "#{@project_dir}/template-1.8.spec", :mock => @maintenance_mock_env
  #rake.on_version "=",  "0.8.7", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  rake.on_version "=",  "0.8.7", "create rpm package", :spec => "#{@project_dir}/template-1.9.spec", :mock => @devel_mock_env
  rake.on_version "=",  "0.8.7", "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel", :delete_rpms => true

  rake.on_version "*",          "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
end
