%global tl_name enigma
%global tl_revision 29802

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Encrypt documents with a three rotor Enigma
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/enigma
License:	bsd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/enigma.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/enigma.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides historical encryption (Enigma cipher) for LuaTeX-
based formats.

