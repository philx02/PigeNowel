set REPODIR=%CD%

set BOOST_ROOT=%BOOST_ROOT_VS2013%

mkdir "%HOMEDRIVE%\%HOMEPATH%\builds\PigeNowel"
pushd "%HOMEDRIVE%\%HOMEPATH%\builds\PigeNowel"
cmake -G "Visual Studio 12" %REPODIR%
popd

