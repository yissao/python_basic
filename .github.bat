@echo off
if '%1' == '' (
    echo %errorlevel%
    goto fim
) else (
    git add .
    git commit -m %1
    git push -u origin main
)

:fim
echo Sem parametros
