Name:		texlive-xindy
Version:	59894
Release:	1
Summary:	A general-purpose index processor
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xindy
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xindy.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xindy.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Xindy was developed after an impasse had been encountered in
the attempt to complete internationalisation of makeindex.
Xindy can be used to process indexes for documents marked up
using (La)TeX, Nroff family and SGML-based languages. Xindy is
highly configurable, both in markup terms and in terms of the
collating order of the text being processed.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/xindy
%{_texmfdistdir}/texmf-dist/scripts/xindy
%doc %{_texmfdistdir}/texmf-dist/doc/xindy
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/xindy.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/xindy.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/texindy.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/texindy.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/tex2xindy.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/tex2xindy.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
