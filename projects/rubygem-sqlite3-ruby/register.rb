# rubygem-sqlite3-ruby polisher registration

project :name => 'rubygem-sqlite3-ruby' do |sqlite3|
  sqlite3.add_gem :name => 'sqlite3', :uri => 'http://rubygems.org/gems/sqlite3-ruby-%{version}.gem', :primary_source => true

  sqlite3.version "*", :depends_on => project(:name => 'ruby')

  sqlite3.on_version "*", "download sources"

  sqlite3.on_version "=", "1.2.4", "create rpm package", :spec => "#{@project_dir}/template-1.2.4.spec", :mock => @stable_mock_env
  sqlite3.on_version "=", "1.2.4", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  sqlite3.on_version ">=", "1.3.0", "create rpm package", :spec => "#{@project_dir}/template-1.3.0.spec", :mock => @maintenance_mock_env
  sqlite3.on_version ">=", "1.3.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  sqlite3.on_version "*", "update yum repo", :repo => "#{@artifacts_dir}/repos/rawhide"
end
