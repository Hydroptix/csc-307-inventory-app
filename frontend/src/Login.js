import React, { Component } from 'react'
import LoginForm from './LoginForm'
import axios from 'axios'

class Login extends Component {
  state = {
    loginAttempted: false
  }

  checkUserExists (username) {
    console.log("Making get call to http://localhost:5000/users?name=" + username)
    return axios.get('http://localhost:5000/users?name=' + username, {name: username})
      .then(function (response) {
        console.log(response)
        return response
      })
      .catch(function (error) {
        console.log(error)
        return false
      })
  }

  attemptLogin = username => {
    console.log("Checking if " + JSON.stringify(username) + " is a user")
    this.checkUserExists(username.username).then(response => {
      if (response.status === 200) {
        if (response.data.users.length > 0) {
          this.props.history.push('/songs')
          return true
        }
      }

      this.setState({
        loginAttempted: true
      })

      return false
    })
  }

  render () {

    if (this.state.loginAttempted) {
      return (
        <div className="container">
          <LoginForm handleSubmit={this.attemptLogin}/>
          <strong style={{ color: 'red' }}>Username not found: please enter a valid username (usernames are case sensitive)</strong>
        </div>
      )
    } else {
      return (
        <div className="container">
          <LoginForm handleSubmit={this.attemptLogin}/>
        </div>
      )
    }
  }

}

export default Login