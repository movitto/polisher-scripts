# ruby-mysql polisher registration

project :name => 'ruby-mysql' do |ruby_mysql|
  ruby_mysql.add_gem :name => 'ruby-mysql', :uri => 'http://tmtm.org/downloads/mysql/ruby/mysql-ruby-%{version}.tar.gz'

  ruby_mysql.on_version "*",           "create rpm package", "#{@project_dir}/template.spec"
  ruby_mysql.on_version "*",           "update yum repo",    "#{@artifacts_dir}/repos/rawhide"
  ruby_mysql.on_version "=",  "2.8",   "update yum repo",    "#{@artifacts_dir}/repos/stable"
  ruby_mysql.on_version "=",  "2.8.2", "update yum repo",    "#{@artifacts_dir}/repos/maintenance"
  ruby_mysql.on_version ">=", "2.8",   "update yum repo",    "#{@artifacts_dir}/repos/devel"
end
