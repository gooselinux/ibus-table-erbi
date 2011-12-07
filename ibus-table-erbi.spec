Name:       ibus-table-erbi
Version:    1.2.0.20090901
Release:    6%{?dist}

Summary:           Erbi input method tables for IBus-Table
Summary(zh_TW):    IBus-Table 二筆碼表
Summary(zh_HK):    IBus-Table 二筆碼表
Summary(zh_CN):    IBus-Table 二笔码表

License:    GPLv2+
Group:      System Environment/Libraries
URL:        http://code.google.com/p/ibus/
Source0:    http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

Requires:         ibus-table >= 1.2
Requires(post):   ibus-table >= 1.2
BuildRequires:    ibus-table-devel >= 1.2

%description
The package contains Erbi input method tables for IBus-Table. 

%description -l zh_CN
本包含有 IBus-Table 二笔码表。

%description -l zh_HK
呢個包有 IBus-Table 二筆碼表。

%description -l zh_TW
此套件包含 IBus-Table 二筆碼表。

%prep
%setup -q

%build
export IBUS_TABLE_CREATEDB="%{_bindir}/ibus-table-createdb --no-create-index"
%configure --prefix=%{_prefix} --enable-erbi --enable-erbi-qs
%__make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} NO_INDEX=true install INSTALL="install -p"

%clean
%__rm -rf %{buildroot}

%post
cd %{_datadir}/ibus-table/tables/
pwd
%{_bindir}/ibus-table-createdb -i -n erbi.db
%{_bindir}/ibus-table-createdb -i -n erbi_qs.db

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_datadir}/ibus-table/tables/erbi.db
%{_datadir}/ibus-table/tables/erbi_qs.db
%{_datadir}/ibus-table/icons/erbi.png
%{_datadir}/ibus-table/icons/erbi-qs.svg

%changelog
* Thu Feb 25 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20090901-6.el6
- Resolves: rhbz#567749
- Fix changelog.

* Thu Feb 25 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20090901-5.el6
- Resolves: rhbz#567749
- Fixes build error with BuildRequires from ibus-table to ibus-table-devel.
- Removes ibus from Requires as ibus-table should have request that.

* Tue Jan 19 2010 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090901-4.fc12
- Resolves: rhbz#556685
- Fixes rpmline errors.

* Tue Jan 19 2010 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090901-3.fc12
- Resolves: rhbz#556685
- Fixes rpmline errors.

* Mon Jan 18 2010 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090901-2.fc12
- Resolves: rhbz#556339
- Fixes rpmlint errors.

* Tue Sep 01 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090901-1.fc12
- Updated source with fixes on format of erbi standard table.

* Mon Aug 31 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090831-1.fc12
- Updated source.

* Fri Aug 28 2009 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20090828-1.fc12
- Updated source with addition of standard ErBi table.
- Corrected Requires package.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20090717-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Caius 'kaio' Chance <k at kaio.me> - 1.1.0.20090717-2.fc12
- Removed unneccessary BuildRequires.
- Removed unneccessary owned directories.
- Changed autogen.sh into configure.

* Fri Jul 17 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090717-1.fc12
- Rebuilt with IBus 1.2.

* Fri Jul 03 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090407-9.fc12
- Fixed index creation at post-install.
- Removed bootstrap.
- Refined package dependencies.
- Added owned directories.
- Replaced hard coded command with macros.

* Mon May 18 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090407-8.fc12
- Rebuilt with index creation during post-install.

* Mon May 18 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090407-7.fc12
- Resolves: rhbz#500973 (Missing .txt during post.)

* Wed Apr 23 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090407-6.fc12
- rebuilt

* Wed Apr 23 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090407-5.fc12
- rebuilt

* Wed Apr 23 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090407-4.fc12
- Refined file properties and updated description.

* Tue Apr 07 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090407-3.fc11
- Fixed files typo.

* Tue Apr 07 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090407-2.fc11
- Updated spec file info.

* Tue Apr 07 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090407-1.fc11
- Corrected license to GPLv2.

* Mon Apr 06 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090403-2.fc11
- Added ChangeLog as doc.

* Thu Apr 02 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090403-1.fc11
- Updated source tarball.

* Thu Apr 02 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090402-1.fc11
- Resolves: rhbz#488173
- Splited from ibus-table.
