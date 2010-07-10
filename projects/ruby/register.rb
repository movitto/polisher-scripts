# ruby polisher registration

project :name => "ruby" do |ruby|
  ruby.add_archive :name => "ruby", :uri => "ftp://ftp.ruby-lang.org/pub/ruby/%{rubyxver}/ruby-%{arcver}.tar.bz2", :primary_source => true

  ruby.add_archive :name => "ruby-manual", :uri => "http://elbereth-hp.hp.infoseek.co.jp/files/ruby/refm/old/2005/ruby-refm-rdp-1.8.2-ja-html.tar.gz" do |archive|
    archive.version "*", :corresponds_to => ruby.version("1.8.6")
  end
  
  ruby.add_archive :name => "ruby-faq", :uri => "ftp://ftp.ruby-lang.org/pub/ruby/doc/rubyfaq-990927.tar.gz" do |archive|
    archive.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_archive :name => "ruby-faq-jp", :uri => "ftp://ftp.ruby-lang.org/pub/ruby/doc/rubyfaq-jp-990927.tar.gz" do |archive|
    archive.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_archive :name => "ruby-tcltk", :uri => "#{@morsiorg_polisher_sources}/ruby-rev%{tcltk_git_version}-ext_tk.tar.gz" do |archive|
    archive.version "*", :tcltk_git_version => "415a3ef9ab82c65a7abc", :corresponds_to => ruby.version("1.8.7")
  end

  ruby.add_file    :name => "ruby-irb-man", :uri => "#{@fedora_cvs}/irb.1?view=co" do |file|
    file.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_file    :name => "ruby-mode-init-el", :uri => "#{@fedora_cvs}/ruby-mode-init.el?view=co" do |file|
    file.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_patch   :name => "ruby-deadcode", :uri => "#{@fedora_cvs}/ruby-deadcode.patch?view=co" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_patch   :name => 'rubyprefix', :uri => "#{@fedora_cvs}/ruby-1.8.6-p383-rubyprefix.patch?view=co" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_patch   :name => 'deprecated-sitelib-search-path', :uri => "#{@fedora_cvs}/ruby-deprecated-sitelib-search-path.patch?view=co" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_patch   :name => 'deprecated-search-path',         :uri => "#{@fedora_cvs}/ruby-deprecated-search-path.patch?view=co" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_patch   :name => 'ruby-multilib',                  :uri => "#{@morsiorg_polisher_sources}/ruby-%{multilib_patch_version}multilib.patch" do |patch|
    patch.version "*", :multilib_patch_version => "",        :corresponds_to => ruby.version("1.8.6")
    patch.version "*", :multilib_patch_version => "1.8.7-",  :corresponds_to => ruby.version("1.8.7")
    patch.version "*", :multilib_patch_version => "1.9.1-",  :corresponds_to => ruby.version("1.9.1")
  end

  ruby.add_patch   :name => 'ruby-rexml',                     :uri => "#{@fedora_cvs}/ruby-1.8.6-rexml-CVE-2008-3790.patch?view=co" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_patch   :name => 'ruby-1.8.6-p287-CVS-2008-5189',  :uri => "#{@fedora_cvs}/ruby-1.8.6-p287-CVE-2008-5189.patch?view=co" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_patch   :name => 'ruby-1.8.6-p287-remove-ssl-rand-range', :uri => "#{@fedora_cvs}/ruby-1.8.6-p287-remove-ssl-rand-range.patch?view=co" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_patch   :name => 'ruby-always-use-i368', :uri => "#{@morsiorg_polisher_sources}/ruby-%{alwaysusei386_patch_version}always-use-i386.patch" do |patch|
    patch.version "*", :alwaysusei386_patch_version => "",            :corresponds_to => ruby.version("1.8.6")
    patch.version "*", :alwaysusei386_patch_version => "1.8.7-",      :corresponds_to => ruby.version("1.8.7")
    patch.version "*", :alwaysusei386_patch_version => "1.9.1-p243-", :corresponds_to => ruby.version("1.9.1")
  end

  ruby.add_patch   :name => 'ruby-openssl', :uri => "#{@morsiorg_polisher_sources}/ruby-%{openssl_patch_version}openssl-1.0.patch" do |patch|
    patch.version "*", :openssl_patch_version => "",            :corresponds_to => ruby.version("1.8.6")
    patch.version "*", :openssl_patch_version => "1.9.1-p243-", :corresponds_to => ruby.version("1.9.1")
  end

  ruby.add_patch   :name => 'ruby-mkmf-use-shared', :uri => "#{@morsiorg_polisher_sources}/ruby-%{mkmf_patch_version}-mkmf-use-shared.patch?view=co" do |patch|
    patch.version "*", :mkmf_patch_version => "1.8.6-p383", :corresponds_to => ruby.version("1.8.6")
    patch.version "*", :mkmf_patch_version => "1.8.7-p249", :corresponds_to => ruby.version("1.8.7")
    patch.version "*", :mkmf_patch_version => "1.9.1",      :corresponds_to => ruby.version("1.9.1")
  end

  ruby.add_patch   :name => 'ruby-1.8.6-p369-ri-gem_multipath', :uri => "#{@fedora_cvs}/ruby-1.8.6-p369-ri-gem_multipath.patch?view=co" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_patch   :name => 'ruby-1.8head-irb-save-history', :uri => "#{@fedora_cvs}/ruby-1.8head-irb-save-history.patch?view=co" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_patch   :name => 'ruby-1.8.6-simplify-openssl-digest', :uri => "#{@fedora_cvs}/ruby-1.8.6-simplify-openssl-digest.patch?view=co" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_patch   :name => 'ruby-1.8.7-libs', :uri => "#{@morsiorg_polisher_sources}/ruby-1.8.7-lib-paths.patch" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.8.7")
  end

  ruby.add_patch   :name => 'ruby-1.9.1-p243-mmt-searchpath', :uri => "#{@morsiorg_polisher_sources}/ruby-1.9.1-p243-mmt-searchpath.patch" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.9.1")
  end

  ruby.add_patch   :name => 'ruby-1.9.1-p243-mmt-searchpath-2', :uri => "#{@morsiorg_polisher_sources}/ruby-1.9.1-p243-mmt-searchpath-2.patch" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.9.1")
  end

  ruby.add_patch   :name => 'ruby-1.9.1-p376-epel-test', :uri => "#{@morsiorg_polisher_sources}/ruby-1.9.1-p376-epel-test.patch" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.9.1")
  end

  # since rubygems was added to ruby 1.9 we need to apply related patches here
  ruby.add_patch   :name => 'ruby-1.9.1-rubygems-noarch-gemdir', :uri => "#{@morsiorg_polisher_sources}/ruby-1.9.1-rubygems-noarch-gemdir.patch" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.9.1")
  end

  ruby.on_version "=", "1.8.6", "download sources", :rubyxver => '1.8', :arcver => '1.8.6-p388'
  ruby.on_version "=", "1.8.7", "download sources", :rubyxver => '1.8', :arcver => '1.8.7-p299'
  ruby.on_version "=", "1.9.1", "download sources", :rubyxver => '1.9', :arcver => '1.9.1-p376'

  ruby.on_version "=", "1.8.6", "create rpm package", :spec => "#{@project_dir}/template-1.8.6.spec", :mock => @system_mock_env, :rubyxver => '1.8', :rubyver => '1.8.6', :patchlevel => '388'
  ruby.on_version "=", "1.8.7", "create rpm package", :spec => "#{@project_dir}/template-1.8.7.spec", :mock => @system_mock_env, :rubyxver => '1.8', :rubyver => '1.8.7', :patchlevel => '299'
  ruby.on_version "=", "1.9.1", "create rpm package", :spec => "#{@project_dir}/template-1.9.1.spec", :mock => @system_mock_env, :rubyxver => '1.9', :rubyver => '1.9.1', :patchlevel => '376'

  ruby.on_version "*",          "update yum repo", :repo => "#{@artifacts_dir}/repos/rawhide"
  ruby.on_version "=", "1.8.6", "update yum repo", :repo => "#{@artifacts_dir}/repos/stable"
  ruby.on_version "=", "1.8.7", "update yum repo", :repo => "#{@artifacts_dir}/repos/maintenance"
  ruby.on_version "=", "1.9.1", "update yum repo", :repo => "#{@artifacts_dir}/repos/devel"
end
