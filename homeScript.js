fetch('05-03-notes.txt')
            .then(response => response.text())
            .then(data => {
                document.getElementById('notes1').textContent = data;
            })
            .catch(error => console.error('Error fetching the text file:', error));