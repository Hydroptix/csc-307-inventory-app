import React, { Component } from 'react'

class LoginForm extends Component {
  initialState = {
    username: ''
  }

  state = this.initialState

  handleChange = event => {
    const { name, value } = event.target

    this.setState({
      [name]: value,
    })
  }

  handleLogin = () => {
    this.props.handleSubmit(this.state)
  }

  handleRegister = () => {
    this.props.handleRegister(this.state)
  }

  render () {
    const { username } = this.state

    return (
      <form>
        <label htmlFor="username">Username</label>
        <input
          type="text"
          name="username"
          id="username"
          value={username}
          onChange={this.handleChange}
        />
        {/* The below view html element allows the buttons to be side by side*/}
        <tr>
          <td>
            <input
              type="button"
              value="Login"
              onClick={this.handleLogin}
            />
          </td>
          <td>
            <input
              type="button"
              value="Register"
              onClick={this.handleRegister}
            />
          </td>

        </tr>
      </form>
    )
  }

}

export default LoginForm