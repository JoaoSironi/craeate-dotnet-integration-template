import os
from time import sleep

respositoryName = input('Repository name: ')
print('Creating repository ' + respositoryName)

os.system(f'dotnet new sln --name Rech.Integration.{respositoryName}')
os.system(f'dotnet new classlib -o Rech.Integration.{respositoryName}.Send')
os.system(f'dotnet new classlib -o Rech.Integration.{respositoryName}.Debugger')

sleep(3)

print('Add Debugger reference and dependencies')

os.system(f'cd Rech.Integration.{respositoryName}.Debugger && dotnet add reference ../Rech.Integration.{respositoryName}.Send/Rech.Integration.{respositoryName}.Send.csproj')
os.system(f'cd Rech.Integration.{respositoryName}.Debugger && dotnet add package Rech.Integration.Base')

print('Add Debugger and Send to solution')

os.system(f'dotnet sln ./Rech.Integration.{respositoryName}.sln add ./Rech.Integration.{respositoryName}.Debugger/Rech.Integration.{respositoryName}.Debugger.csproj')
os.system(f'dotnet sln ./Rech.Integration.{respositoryName}.sln add ./Rech.Integration.{respositoryName}.Send/Rech.Integration.{respositoryName}.Send.csproj')

print('Add Send dependencies')

os.system(f'cd Rech.Integration.{respositoryName}.Send && dotnet add package Rech.Integration.Generic')