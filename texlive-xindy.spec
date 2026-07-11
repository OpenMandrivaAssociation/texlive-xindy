%global tl_name xindy
%global tl_revision 78957

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.5.1
Release:	%{tl_revision}.1
Summary:	A general-purpose index processor
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/indexing/xindy/base
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xindy.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xindy.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(xindy.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Xindy was developed after an impasse had been encountered in the attempt
to complete internationalisation of makeindex. Xindy can be used to
process indexes for documents marked up using (La)TeX, Nroff family and
SGML-based languages. Xindy is highly configurable, both in markup terms
and in terms of the collating order of the text being processed.

