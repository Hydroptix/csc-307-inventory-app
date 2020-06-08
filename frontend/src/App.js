import React, { Suspense, lazy } from 'react'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

const Login = lazy(() => import('./Login'))
const AllSongs = lazy(() => import('./AllSongs'))

const App = () => (
  <Router>
    <Suspense fallback={<div>Loading...</div>}>
      <Switch>
        <Route exact path="/" component={Login}/>
        <Route path="/songs" component={AllSongs}/>
      </Switch>
    </Suspense>
  </Router>
)

export default App
