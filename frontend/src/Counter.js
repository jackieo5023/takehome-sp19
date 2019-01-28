import React, { Component } from 'react'

class Counter extends Component {
  // YOUR CODE GOES BELOW
  state = {
    count: this.props.initialCount
  }

  handleIncrement = () => {
    this.setState({
      count: this.state.count + 1
    });
  }

  handleDecrement = () => {
    this.setState({
      count: this.state.count - 1
    });
  }
  
  render() {
    return (
      <div>
        Count: {this.state.count}
        <button onClick={this.handleIncrement}>+</button>
        <button onClick={this.handleDecrement}>-</button>
      </div>
    )
  }
}

export default Counter
