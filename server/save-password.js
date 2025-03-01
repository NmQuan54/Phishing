const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();

app.use(express.urlencoded({ extended: true }));

app.post('/save-password', (req, res) => {
    const { email, password } = req.body;
    const data = `Email: ${email}, Password: ${password}\n`;

    fs.appendFile(path.join(__dirname, 'passwords.txt'), data, (err) => {
        if (err) {
            console.error('Error saving data:', err);
            return res.status(500).send('There was an error saving your data.');
        }
        res.send('Your data has been saved successfully.');
    });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
