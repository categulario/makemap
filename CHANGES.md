# Cómo renderear la cuadrícula UTM sin morir en el intento

De este branch, tomar el [tilestache/config.cfg](https://github.com/categulario/makemap/blob/master/tilestache/tilestache-mapbox.cfg)

Tuve que modificar la [línea 60 del tile provider](https://github.com/categulario/makemap/blob/feature/use-tilestache-layers/tile_provider.py#L60) creo que de todas formas es buena idea dejar el valor de la capa de tilestache en algo genérico para que después la decisión de las capas a usar se haga en el `tilestache.cfg`. La otra opción es poder configurar la capa de tilestache en tiempo de ejecución con una bandera o algo.

Y aquí viene lo bueno, para que tilestache pudiera hacer el sandwich necesité [Blit](http://github.com/migurski/Blit) pero está viejo y mi archlinux tiene lo último de lo último, así que tuve que hacerlo funcionar [con este otro blit](https://github.com/migurski/Blit/pull/2/files). Lo que hace es ofrecer alguna capa de abstracción entre tilestache y PIL para crear las imágenes y en este caso ensaduicharlas.

Creo que eso fue todo.
