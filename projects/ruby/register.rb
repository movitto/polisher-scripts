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

  ruby.add_patch   :name => 'ruby-multilib',                  :uri => "#{@fedora_cvs}/ruby-multilib.patch?view=co" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.8.6")
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
    patch.version "*", :alwaysusei386_patch_version => "1.9.1-p243-", :corresponds_to => ruby.version("1.9.1")
  end

  ruby.add_patch   :name => 'ruby-openssl', :uri => "#{@morsiorg_polisher_sources}/ruby-%{openssl_patch_version}openssl-1.0.patch" do |patch|
    patch.version "*", :openssl_patch_version => "",            :corresponds_to => ruby.version("1.8.6")
    patch.version "*", :openssl_patch_version => "1.9.1-p243-", :corresponds_to => ruby.version("1.9.1")
  end

  ruby.add_patch   :name => 'ruby-1.8.6-p369-ri-gem_multipath', :uri => "#{@fedora_cvs}/ruby-1.8.6-p369-ri-gem_multipath.patch?view=co" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_patch   :name => 'ruby-1.8head-irb-save-history', :uri => "#{@fedora_cvs}/ruby-1.8head-irb-save-history.patch?view=co" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_patch   :name => 'ruby-1.8.6-p383-mkmf-use-shared', :uri => "#{@fedora_cvs}/ruby-1.8.6-p383-mkmf-use-shared.patch?view=co" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.8.6")
  end

  ruby.add_patch   :name => 'ruby-1.8.6-simplify-openssl-digest', :uri => "#{@fedora_cvs}/ruby-1.8.6-simplify-openssl-digest.patch?view=co" do |patch|
    patch.version "*", :corresponds_to => ruby.version("1.8.6")
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

  ruby.on_version "=", "1.8.6", "create rpm package", "#{@project_dir}/template-1.8.6.spec"
  #ruby.on_version "=", "1.8.7", "create rpm package", "#{@project_dir}/template-1.8.7.spec" # TODO
  ruby.on_version ">=", "1.9.1", "create rpm package", "#{@project_dir}/template-1.9.1.spec"

  ruby.on_version "*",           "update yum repo", "#{@artifacts_dir}/repos/rawhide"
  ruby.on_version "=",  "1.8.6", "update yum repo", "#{@artifacts_dir}/repos/stable"
  ruby.on_version "=",  "1.8.7", "update yum repo", "#{@artifacts_dir}/repos/maintenance"
  ruby.on_version ">=", "1.9.1", "update yum repo", "#{@artifacts_dir}/repos/devel"
end
