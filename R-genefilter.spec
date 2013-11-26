%define		packname	genefilter

Summary:	Methods for filtering genes from microarray experiments
Name:		R-%{packname}
Version:	1.44.0
Release:	1
License:	Artistic 2.0
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	9b368a3942b705cc1547c2c36ddc23ee
URL:		http://bioconductor.org/packages/release/bioc/html/genefilter.html
BuildRequires:	R
BuildRequires:	R-Biobase
BuildRequires:	R-AnnotationDbi
BuildRequires:	R-annotate
BuildRequires:	R-hgu95av2.db
BuildRequires:	R-ALL
BuildRequires:	R-ROC
BuildRequires:	R-tkWidgets
BuildRequires:	texlive-latex
BuildRequires:	zlib-devel
Requires:	R
Requires:	R-Biobase
Requires:	R-AnnotationDbi
Requires:	R-annotate
Suggests:	R-hgu95av2.db
Suggests:	R-ALL
Suggests:	R-ROC
Suggests:	R-tkWidgets
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Some basic functions for filtering genes.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/wFun
%dir %{_libdir}/R/library/%{packname}/libs
%attr(755,root,root) %{_libdir}/R/library/%{packname}/libs/%{packname}.so
