# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/umthesis
# catalog-date 2009-09-17 20:11:38 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-umthesis
Version:	0.2
Release:	1
Summary:	Dissertations at the University of Michigan
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/umthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umthesis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The class loads book class, and makes minimal changes to it;
its coding aims to be as robust as possible, and as a result it
has few conflicts with potential add-on packages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/umthesis/umthesis.cls
%doc %{_texmfdistdir}/doc/latex/umthesis/PDP.tex
%doc %{_texmfdistdir}/doc/latex/umthesis/README
%doc %{_texmfdistdir}/doc/latex/umthesis/appendix.tex
%doc %{_texmfdistdir}/doc/latex/umthesis/conclusion.tex
%doc %{_texmfdistdir}/doc/latex/umthesis/example.pdf
%doc %{_texmfdistdir}/doc/latex/umthesis/example.tex
%doc %{_texmfdistdir}/doc/latex/umthesis/exp1.tex
%doc %{_texmfdistdir}/doc/latex/umthesis/exp2.tex
%doc %{_texmfdistdir}/doc/latex/umthesis/exp3.tex
%doc %{_texmfdistdir}/doc/latex/umthesis/felty.bib
%doc %{_texmfdistdir}/doc/latex/umthesis/intro.tex
%doc %{_texmfdistdir}/doc/latex/umthesis/mybibstyle.bst
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
