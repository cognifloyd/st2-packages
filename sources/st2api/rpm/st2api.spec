%define package st2api
%define _sourcedir /root/code
%define specdir /root/code/rpmspec
%include %{specdir}/package_top.spec

Summary: St2Api - StackStorm API component
Requires: st2common = %{version}-%{release}

%include %{specdir}/package_venv.spec
%include %{specdir}/helpers.spec

%description
  <insert long description, indented with spaces>

%install
  %default_install
  %pip_install_venv

  # systemd service file
  mkdir -p %{buildroot}%{_unitdir}
  install -m0644 %{SOURCE0}/rpm/st2api.service %{buildroot}%{_unitdir}/st2api.service
  make post_install DESTDIR=%{?buildroot}

%prep
  rm -rf %{buildroot}
  mkdir -p %{buildroot}

%clean
  rm -rf %{buildroot}

%pre
  %inst_venv_divertions

%preun
  %systemd_preun st2api.service

%postun
  %uninst_venv_divertions
  %systemd_postun

%files
  %{_bindir}/*
  %{_datadir}/python/%{name}
  %config(noreplace) %{_sysconfdir}/%{name}/*
  %{_unitdir}/%{name}.service