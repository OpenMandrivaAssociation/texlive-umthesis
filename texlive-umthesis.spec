%global tl_name umthesis
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Dissertations at the University of Michigan
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/umthesis
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/umthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/umthesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class loads book class, and makes minimal changes to it; its coding
aims to be as robust as possible, and as a result it has few conflicts
with potential add-on packages.

