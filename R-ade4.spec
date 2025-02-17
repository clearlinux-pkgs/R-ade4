#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: e36a856
#
Name     : R-ade4
Version  : 1.7.23
Release  : 71
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/ade4_1.7-23.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/ade4_1.7-23.tar.gz
Summary  : Analysis of Ecological Data: Exploratory and Euclidean Methods
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-ade4-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppArmadillo
Requires: R-pixmap
Requires: R-sp
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : R-RcppArmadillo-dev
BuildRequires : R-pixmap
BuildRequires : R-sp
BuildRequires : buildreq-R

%description
No detailed description available

%package dev
Summary: dev components for the R-ade4 package.
Group: Development
Requires: R-ade4-lib = %{version}-%{release}
Provides: R-ade4-devel = %{version}-%{release}
Requires: R-ade4 = %{version}-%{release}

%description dev
dev components for the R-ade4 package.


%package lib
Summary: lib components for the R-ade4 package.
Group: Libraries

%description lib
lib components for the R-ade4 package.


%prep
%setup -q -n ade4
pushd ..
cp -a ade4 buildavx2
popd
pushd ..
cp -a ade4 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1739828645

%install
export SOURCE_DATE_EPOCH=1739828645
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ade4/CITATION
/usr/lib64/R/library/ade4/DESCRIPTION
/usr/lib64/R/library/ade4/INDEX
/usr/lib64/R/library/ade4/Meta/Rd.rds
/usr/lib64/R/library/ade4/Meta/data.rds
/usr/lib64/R/library/ade4/Meta/features.rds
/usr/lib64/R/library/ade4/Meta/hsearch.rds
/usr/lib64/R/library/ade4/Meta/links.rds
/usr/lib64/R/library/ade4/Meta/nsInfo.rds
/usr/lib64/R/library/ade4/Meta/package.rds
/usr/lib64/R/library/ade4/Meta/vignette.rds
/usr/lib64/R/library/ade4/NAMESPACE
/usr/lib64/R/library/ade4/NEWS.md
/usr/lib64/R/library/ade4/R/ade4
/usr/lib64/R/library/ade4/R/ade4.rdb
/usr/lib64/R/library/ade4/R/ade4.rdx
/usr/lib64/R/library/ade4/WORDLIST
/usr/lib64/R/library/ade4/data/abouheif.eg.rda
/usr/lib64/R/library/ade4/data/acacia.rda
/usr/lib64/R/library/ade4/data/aminoacyl.rda
/usr/lib64/R/library/ade4/data/apis108.rda
/usr/lib64/R/library/ade4/data/aravo.rda
/usr/lib64/R/library/ade4/data/ardeche.rda
/usr/lib64/R/library/ade4/data/arrival.rda
/usr/lib64/R/library/ade4/data/atlas.rda
/usr/lib64/R/library/ade4/data/atya.rda
/usr/lib64/R/library/ade4/data/avijons.rda
/usr/lib64/R/library/ade4/data/avimedi.rda
/usr/lib64/R/library/ade4/data/aviurba.rda
/usr/lib64/R/library/ade4/data/bacteria.rda
/usr/lib64/R/library/ade4/data/banque.rda
/usr/lib64/R/library/ade4/data/baran95.rda
/usr/lib64/R/library/ade4/data/bf88.rda
/usr/lib64/R/library/ade4/data/bordeaux.rda
/usr/lib64/R/library/ade4/data/bsetal97.rda
/usr/lib64/R/library/ade4/data/buech.rda
/usr/lib64/R/library/ade4/data/butterfly.rda
/usr/lib64/R/library/ade4/data/capitales.rda
/usr/lib64/R/library/ade4/data/carni19.rda
/usr/lib64/R/library/ade4/data/carni70.rda
/usr/lib64/R/library/ade4/data/carniherbi49.rda
/usr/lib64/R/library/ade4/data/casitas.rda
/usr/lib64/R/library/ade4/data/chatcat.rda
/usr/lib64/R/library/ade4/data/chats.rda
/usr/lib64/R/library/ade4/data/chazeb.rda
/usr/lib64/R/library/ade4/data/chevaine.rda
/usr/lib64/R/library/ade4/data/chickenk.rda
/usr/lib64/R/library/ade4/data/clementines.rda
/usr/lib64/R/library/ade4/data/cnc2003.rda
/usr/lib64/R/library/ade4/data/coleo.rda
/usr/lib64/R/library/ade4/data/corvus.rda
/usr/lib64/R/library/ade4/data/datalist
/usr/lib64/R/library/ade4/data/deug.rda
/usr/lib64/R/library/ade4/data/doubs.rda
/usr/lib64/R/library/ade4/data/dunedata.rda
/usr/lib64/R/library/ade4/data/ecg.rda
/usr/lib64/R/library/ade4/data/ecomor.rda
/usr/lib64/R/library/ade4/data/elec88.rda
/usr/lib64/R/library/ade4/data/escopage.rda
/usr/lib64/R/library/ade4/data/euro123.rda
/usr/lib64/R/library/ade4/data/fission.rda
/usr/lib64/R/library/ade4/data/friday87.rda
/usr/lib64/R/library/ade4/data/fruits.rda
/usr/lib64/R/library/ade4/data/ggtortoises.rda
/usr/lib64/R/library/ade4/data/granulo.rda
/usr/lib64/R/library/ade4/data/hdpg.rda
/usr/lib64/R/library/ade4/data/houmousr.rda
/usr/lib64/R/library/ade4/data/housetasks.rda
/usr/lib64/R/library/ade4/data/humDNAm.rda
/usr/lib64/R/library/ade4/data/ichtyo.rda
/usr/lib64/R/library/ade4/data/irishdata.rda
/usr/lib64/R/library/ade4/data/julliot.rda
/usr/lib64/R/library/ade4/data/jv73.rda
/usr/lib64/R/library/ade4/data/kcponds.rda
/usr/lib64/R/library/ade4/data/lascaux.rda
/usr/lib64/R/library/ade4/data/lizards.rda
/usr/lib64/R/library/ade4/data/macaca.rda
/usr/lib64/R/library/ade4/data/macon.rda
/usr/lib64/R/library/ade4/data/macroloire.rda
/usr/lib64/R/library/ade4/data/mafragh.rda
/usr/lib64/R/library/ade4/data/maples.rda
/usr/lib64/R/library/ade4/data/mariages.rda
/usr/lib64/R/library/ade4/data/meau.rda
/usr/lib64/R/library/ade4/data/meaudret.rda
/usr/lib64/R/library/ade4/data/microsatt.rda
/usr/lib64/R/library/ade4/data/mjrochet.rda
/usr/lib64/R/library/ade4/data/mollusc.rda
/usr/lib64/R/library/ade4/data/monde84.rda
/usr/lib64/R/library/ade4/data/morphosport.rda
/usr/lib64/R/library/ade4/data/newick.eg.rda
/usr/lib64/R/library/ade4/data/njplot.rda
/usr/lib64/R/library/ade4/data/olympic.rda
/usr/lib64/R/library/ade4/data/oribatid.rda
/usr/lib64/R/library/ade4/data/ours.rda
/usr/lib64/R/library/ade4/data/palm.rda
/usr/lib64/R/library/ade4/data/pap.rda
/usr/lib64/R/library/ade4/data/pcw.rda
/usr/lib64/R/library/ade4/data/perthi02.rda
/usr/lib64/R/library/ade4/data/piosphere.rda
/usr/lib64/R/library/ade4/data/presid2002.rda
/usr/lib64/R/library/ade4/data/procella.rda
/usr/lib64/R/library/ade4/data/rankrock.rda
/usr/lib64/R/library/ade4/data/rhizobium.rda
/usr/lib64/R/library/ade4/data/rhone.rda
/usr/lib64/R/library/ade4/data/rpjdl.rda
/usr/lib64/R/library/ade4/data/santacatalina.rda
/usr/lib64/R/library/ade4/data/sarcelles.rda
/usr/lib64/R/library/ade4/data/seconde.rda
/usr/lib64/R/library/ade4/data/skulls.rda
/usr/lib64/R/library/ade4/data/steppe.rda
/usr/lib64/R/library/ade4/data/syndicats.rda
/usr/lib64/R/library/ade4/data/t3012.rda
/usr/lib64/R/library/ade4/data/tarentaise.rda
/usr/lib64/R/library/ade4/data/taxo.eg.rda
/usr/lib64/R/library/ade4/data/tintoodiel.rda
/usr/lib64/R/library/ade4/data/tithonia.rda
/usr/lib64/R/library/ade4/data/tortues.rda
/usr/lib64/R/library/ade4/data/toxicity.rda
/usr/lib64/R/library/ade4/data/trichometeo.rda
/usr/lib64/R/library/ade4/data/ungulates.rda
/usr/lib64/R/library/ade4/data/vegtf.rda
/usr/lib64/R/library/ade4/data/veuvage.rda
/usr/lib64/R/library/ade4/data/westafrica.rda
/usr/lib64/R/library/ade4/data/woangers.rda
/usr/lib64/R/library/ade4/data/worksurv.rda
/usr/lib64/R/library/ade4/data/yanomama.rda
/usr/lib64/R/library/ade4/data/zealand.rda
/usr/lib64/R/library/ade4/doc/faq.R
/usr/lib64/R/library/ade4/doc/faq.Rmd
/usr/lib64/R/library/ade4/doc/faq.html
/usr/lib64/R/library/ade4/doc/index.html
/usr/lib64/R/library/ade4/help/AnIndex
/usr/lib64/R/library/ade4/help/ade4.rdb
/usr/lib64/R/library/ade4/help/ade4.rdx
/usr/lib64/R/library/ade4/help/aliases.rds
/usr/lib64/R/library/ade4/help/figures/logo.svg
/usr/lib64/R/library/ade4/help/paths.rds
/usr/lib64/R/library/ade4/html/00Index.html
/usr/lib64/R/library/ade4/html/R.css
/usr/lib64/R/library/ade4/pictures/atyacarto.pnm
/usr/lib64/R/library/ade4/pictures/atyadigi.pnm
/usr/lib64/R/library/ade4/pictures/avijonseau.pnm
/usr/lib64/R/library/ade4/pictures/avijonsrou.pnm
/usr/lib64/R/library/ade4/pictures/avijonsveg.pnm
/usr/lib64/R/library/ade4/pictures/avijonsvil.pnm
/usr/lib64/R/library/ade4/pictures/butterfly.pnm
/usr/lib64/R/library/ade4/pictures/capitales.pnm
/usr/lib64/R/library/ade4/pictures/fatala.pnm
/usr/lib64/R/library/ade4/pictures/france_sm00.pnm
/usr/lib64/R/library/ade4/pictures/ireland.pnm
/usr/lib64/R/library/ade4/pictures/paris.pnm
/usr/lib64/R/library/ade4/pictures/sarcelles.pnm
/usr/lib64/R/library/ade4/pictures/tintoodiel.pnm

%files dev
%defattr(-,root,root,-)
/usr/lib64/R/library/ade4/include/ade4libCpp.h

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/ade4/libs/ade4.so
/V4/usr/lib64/R/library/ade4/libs/ade4.so
/usr/lib64/R/library/ade4/libs/ade4.so
