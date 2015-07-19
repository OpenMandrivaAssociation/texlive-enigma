# revision 29802
# category Package
# catalog-ctan /macros/luatex/generic/enigma
# catalog-date 2013-04-09 15:55:17 +0200
# catalog-license bsd
# catalog-version 0.1
Name:		texlive-enigma
Version:	0.1
Release:	9
Summary:	Encrypt documents with a three rotor Enigma
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/enigma
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enigma.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enigma.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides historical encryption (Enigma cipher) for
LuaTeX-based formats.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/context/lua/third/enigma/mtx-t-enigma.lua/mtx-t-enigma.lua
%{_texmfdistdir}/tex/context/third/enigma/t-enigma.mkv/t-enigma.mkvi
%{_texmfdistdir}/tex/generic/enigma/enigma.lua
%{_texmfdistdir}/tex/latex/enigma/enigma.sty
%{_texmfdistdir}/tex/plain/enigma/enigma.tex
%doc %{_texmfdistdir}/doc/context/third/enigma/enigma/COPYING
%doc %{_texmfdistdir}/doc/context/third/enigma/enigma/README
%doc %{_texmfdistdir}/doc/context/third/enigma/enigma/enigma-doc.pdf
%doc %{_texmfdistdir}/doc/context/third/enigma/enigma/enigma_manual.tex
%doc %{_texmfdistdir}/doc/context/third/enigma/enigma/examples/enigma-example-context.tex
%doc %{_texmfdistdir}/doc/context/third/enigma/enigma/examples/enigma-example-latex.tex
%doc %{_texmfdistdir}/doc/context/third/enigma/enigma/examples/enigma-example-plain.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc %{buildroot}%{_texmfdistdir}
