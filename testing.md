Pensamientos de cómo probar automáticamente estos ejercicios en el futuro.

Queremos descargar el fork de alguien y correr todo el python para comprobar
cuáles ejercicios ha terminado.

Pero ejecutar Python no confiable es peligroso. Así que tendremos que
ejecutarlo en un entorno seguro.

http://stackoverflow.com/questions/35322452/is-there-a-way-to-sandbox-test-execution-with-pytest-especially-filesystem-acce

> The absolute minimal (but opinionated) approach I devised is the following:
>
> * build a python docker image with:
>   * a dedicated non-root user: pytest
>   * all project dependencies from requirements.txt
>   * the project installed in develop mode
>   * run py.test in a container that mounts the project folder on the host as the home of pytest user
