# rubygem-activerecord polisher registration

project :name => 'rubygem-activerecord' do |activerecord|
  activerecord.add_gem :name => 'activerecord', :uri => 'http://rubygems.org/downloads/activerecord-%{version}.gem', :primary_source => true

  activerecord.add_patch :name => "activerecord-2.3.8-sqlite3-compat.patch", :uri => "#{@morsiorg_polisher_sources}/activerecord-2.3.8-sqlite3-compat.patch" do |patch|
    patch.version "*", :corresponds_to => activerecord.version("2.3.8")
  end

  # see comment in %check section in template-3.0.0
  #activerecord.add_file :name => "activerecord-rakefile", :uri => "http://github.com/rails/rails/raw/master/activerecord/Rakefile" do |file|
  #  file.version "*", :corresponds_to => activerecord.version("3.0.0.beta4")
  #end

  activerecord.on_version "*",           "download sources"

  activerecord.on_version "=",  "2.3.8", "create rpm package", :spec => "#{@project_dir}/template-2.3.8.spec", :mock => @stable_mock_env
  activerecord.on_version "=",  "2.3.8", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  activerecord.on_version "=",  "2.3.8", "create rpm package", :spec => "#{@project_dir}/template-2.3.8.spec", :mock => @maintenance_mock_env
  activerecord.on_version "=",  "2.3.8", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  activerecord.on_version ">=",  "3.0.0", "create rpm package", :spec => "#{@project_dir}/template-3.0.0.spec", :mock => @maintenance_mock_env
  activerecord.on_version ">=",  "3.0.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  # uncomment when Ruby 1.9 supports rails 3
  #activerecord.on_version ">=",  "3.0.0", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @devel_mock_env
  #activerecord.on_version ">=", "3.0.0",  "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"

  activerecord.on_version "*",           "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
end
