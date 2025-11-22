Set-ExecutionPolicy RemoteSigned

python -m venv kivy_env ///////    py -3.11 -m venv kivy_311_env

.\kivy_311_env\Scripts\activate
.\kivy_env\bin\Activate.ps1


#desactivar 
deactivate

#eliminar 
Remove-Item -Recurse -Force .\kivy_env



pip install kivy
python -c "import kivy; print(kivy.__version__)"

