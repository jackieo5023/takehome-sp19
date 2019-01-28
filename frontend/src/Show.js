import React, { Component } from 'react'
import Counter from './Counter'

class App extends Component {
  // YOUR CODE GOES BELOW
  
  render() {
    return (
      <div>
        {this.props.name}
        <Counter initialCount={this.props.episodes_seen} />
      </div>
    )
  }
}

export default App
