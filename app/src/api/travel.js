import Abstract from "./abstract";
import axios from 'axios';

export default class Travel extends Abstract {
  constructor() {
    super();
    this.constants.ENDPOINT = `${this.constants.API_URL}/travel-recommendations`;
    this.data = null;
  }

  /**
   * Fetch travel recommendation data from the remote API.
   * @param {string} season 
   * @param {string} country 
   * @returns {Promise}
  */
  async fetchData(season, country) {
    try {
      const response = await axios.get(`${this.constants.ENDPOINT}?country=${country}&season=${season}`);
      return response.data;
    } catch (error) {
      console.error('Error fetching data:', error);
      throw error;
    }
  }

}
