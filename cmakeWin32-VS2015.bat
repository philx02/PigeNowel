set REPODIR=%CD%

set BOOST_LIBRARYDIR=%BOOST_ROOT%\lib32-msvc-14.0

mkdir "%HOMEDRIVE%\%HOMEPATH%\builds\PigeNowel"
pushd "%HOMEDRIVE%\%HOMEPATH%\builds\PigeNowel"
cmake -G "Visual Studio 14" %REPODIR%
popd

