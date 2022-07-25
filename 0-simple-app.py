import justpy as jp

#quasar style framework

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Analysis of Course Reviews", classes = "text-h3 text-center q-pa-md")      #division
    p1 = jp.QDiv(a = wp, text = "These graphs represent course review analysis")                               #division

    return wp

#wp is a quasar instance

jp.justpy(app)