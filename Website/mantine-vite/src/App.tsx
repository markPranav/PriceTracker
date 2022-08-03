import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import { MantineProvider, Text } from '@mantine/core'
import HomeScreen from './UI/home_screen'

function App() {
  const [count, setCount] = useState(0)

  return (
    <MantineProvider withGlobalStyles withNormalizeCSS>
      <HomeScreen/>
    </MantineProvider>
  )
}

export default App
