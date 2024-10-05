def test_function():
    def i_f():
        print('in area function - test_function')
    i_f() #при воспроизведении функции i_f вне функции test_function не будет возвращать тк.
    # имеются различия пространста имен

test_function()