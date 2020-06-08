import React, { Component } from 'react'
import LoginForm from './LoginForm'
import axios from 'axios'

class Login extends Component {
  state = {
    errorMessage: ''
  }

  checkUserExists (username) {
    console.log('Making get call to http://localhost:5000/users?name=' + username)
    return axios.get('http://localhost:5000/users?name=' + username, { name: username })
      .then(function (response) {
        console.log(response)
        return response
      })
      .catch(function (error) {
        console.log(error)
        return false
      })
  }

  registerUser (username) {
    return axios.post('http://localhost:5000/users', { name: username })
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
    console.log('Checking if ' + JSON.stringify(username) + ' is a user')
    this.checkUserExists(username.username).then(response => {
      if (response.status === 200) {
        if (response.data.users.length > 0) {
          this.props.history.push('/songs')
          return true
        }
      }

      this.setState({
        errorMessage: 'Username not found: please register or enter a valid username'
      })

      return false
    })
  }

  attemptRegister = username => {
    console.log('Checking if ' + JSON.stringify(username) + ' is a user')

    if(username.username === "") {
      this.setState({
        errorMessage: "Please enter a username to register"
      })
      return
    }

    this.checkUserExists(username.username).then(response => {
      if (response.status === 200) {

        // If a user with this name is found, show an error
        if (response.data.users.length > 0) {
          this.setState({
            errorMessage: 'That username already exists: please choose another username'
          })

        } else {
          this.registerUser(username.username).then(response => {
            if (response.status === 201) {
              this.setState({
                errorMessage: 'User registered successfully!'
              })
            }
          })
        }
      }
    })
  }

  render () {

    return (
      <div className="container">
        <LoginForm
          handleSubmit={this.attemptLogin}
          handleRegister={this.attemptRegister}/>
        <strong style={{ color: 'red' }}>{this.state.errorMessage}</strong>
      </div>
    )
  }

}

export default Login