// Importing react and external library 
import React, { useState } from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';

// Importing modules
import TravelAppAPI from '../api';

//Importing external css file
import './index.css'

const View = () => {
  const [country, setCountry] = useState('');
  const [data, setData] = useState([]);
  const [error, setError] = useState('');
  const [season, setSeason] = useState('');

  /**
  * Handle a change in the selected season.
  * @param {Event}
  * @returns {void}
  */
  const _handleSeasonChange = (event) => {
    let season = event.target.value;
    if (season === 'winter' || season === 'summer' || season === 'spring' || season === 'autumn') {
      setError('');
    } else if (season.length >= 3) {
      setError('Please enter a valid season (winter, summer, autumn or spring).');
    }

    setSeason(event.target.value);
  };

  /**
   * Handle a change in the selected country.
   * @param {Event}
   * @returns {void}
   */
  const _handleCountryChange = (event) => {
    setCountry(event.target.value);
  };

  /**
   * Load data from a remote API based on the selected season and country.
   * @returns {Promise}
   */
  const _loadData = async () => {
    try {
      const res = await TravelAppAPI.Travel.fetchData(season, country);
      setData(res);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }

  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="xl">
        <Box className="container">
          <Grid container spacing={2}>
            <Grid item xs={6}>
              <TextField
                label="Country"
                variant="outlined"
                fullWidth
                value={country}
                onChange={_handleCountryChange}
                className="text-field"
              />
            </Grid>
            <Grid item xs={6}>
              <TextField
                label="Season"
                variant="outlined"
                fullWidth
                value={season}
                onChange={_handleSeasonChange}
                className="text-field"
                error={(!!error && season.length >= 3)}
                helperText={error}
              />
            </Grid>
            <Grid item >
              <Button
                variant="contained"
                color="primary"
                onClick={() => _loadData()}
                className="button"
                fullWidth
              >
                Search
              </Button>
            </Grid>
          </Grid>
          <div style={{ marginTop: '25px' }}>
            {data?.recommendations?.map((item, index) => (
              <div key={item}>
                {`${index + 1} : ${item}`}
              </div>
            ))}
          </div>
        </Box>
      </Container>
    </React.Fragment>

  );
};

export default View;
