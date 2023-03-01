- I have words and their definitions in uzbek. I want to build web application to search a word and see its meaning. Can you write code for this application?

```javascript
import React, { useState, useEffect } from 'react';

const wordDefinitions = {};

function App() {
  const [word, setWord] = useState('');
  const [definition, setDefinition] = useState('');

  useEffect(() => {
    const files = [
    'C:\\wordDefinitions\\wordDefinitions1.json',
    'C:\\wordDefinitions\\wordDefinitions2.json'
    ];

    Promise.all(files.map(file => fetch(file).then(response => response.json())))
      .then(data => {
        data.forEach(defs => Object.assign(wordDefinitions, defs));
      });
  }, []);

  const handleSubmit = event => {
    event.preventDefault();
    setDefinition(wordDefinitions[word] || 'Word not found');
  };

  return (
    <div>
      <h1>Word Definition</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" value={word} onChange={e => setWord(e.target.value)} />
        <button type="submit">Search</button>
      </form>
      {definition && <p>Definition: {definition}</p>}
    </div>
  );
}

export default App;
```