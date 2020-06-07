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

  handleSubmit = () => {
    this.props.handleSubmit(this.state)
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
        <input
          type="button"
          value="Login"
          onClick={this.handleSubmit}
        />
      </form>
    )
  }

}

export default LoginForm