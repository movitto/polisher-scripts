# ruby-mysql polisher registration

project :name => 'ruby-mysql' do |ruby_mysql|
  ruby_mysql.add_archive :name => 'ruby-mysql', :uri => 'http://tmtm.org/downloads/mysql/ruby/mysql-ruby-%{version}.tar.gz'

  ruby_mysql.version "*", :depends_on => project(:name => 'ruby')

  ruby_mysql.on_version "*",           "download sources"

  ruby_mysql.on_version "=",  "2.8",   "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @stable_mock_env
  ruby_mysql.on_version "=",  "2.8",   "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  # TODO uncomment when ruby 1.8.7 is setup in maintenance repo
  #ruby_mysql.on_version "=",  "2.8.2", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @maintentance_mock_env
  #ruby_mysql.on_version "=",  "2.8.2", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  ruby_mysql.on_version ">", "2.8",   "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @devel_mock_env
  ruby_mysql.on_version ">", "2.8",   "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"

  ruby_mysql.on_version "*",           "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
end
