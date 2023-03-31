Name:		texlive-umthesis
Version:	15878
Release:	2
Summary:	Dissertations at the University of Michigan
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/umthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class loads book class, and makes minimal changes to it;
its coding aims to be as robust as possible, and as a result it
has few conflicts with potential add-on packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
