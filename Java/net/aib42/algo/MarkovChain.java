package net.aib42.algo;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Random;

public class MarkovChain<I, O>
{
	public class PossibleOutput
		implements Comparable<PossibleOutput>
	{
		double cumulativeProbability;
		O output;

		public PossibleOutput(double p_cumulativeProbability, O p_output) {
			cumulativeProbability = p_cumulativeProbability;
			output = p_output;
		}

		double getCumulativeProbability() {
			return cumulativeProbability;
		}

		O getOutput() {
			return output;
		}

		@Override
		public int compareTo(PossibleOutput rhs) {
			return Double.compare(cumulativeProbability, rhs.cumulativeProbability);
		}
	}

	protected Random random;
	protected Map<I, Map<O, Integer>> inputMap;
	protected Map<I, ArrayList<PossibleOutput>> compiledInputMap;

	public MarkovChain()
	{
		random = new Random();
		inputMap = new HashMap<I, Map<O, Integer>>();
		compiledInputMap = null;
	}

	public void addData(I in, O out)
	{
		addData(in, out, 1);
	}

	public void addData(I in, O out, int count)
	{
		Map<O, Integer> outputMap = inputMap.get(in);

		if (outputMap == null) {
			outputMap = new HashMap<O, Integer>();
			inputMap.put(in, outputMap);
		}

		Integer encounters = outputMap.get(out);

		if (encounters == null) {
			encounters = new Integer(count);
		} else {
			encounters += count;
		}

		outputMap.put(out, encounters);
	}

	public void compile()
	{
		compiledInputMap = new HashMap<I, ArrayList<PossibleOutput>>();

		for (Entry<I, Map<O, Integer>> inputEntry : inputMap.entrySet()) {
			Map<O, Integer> outputMap = inputEntry.getValue();

			int totalEncounters = 0;
			for (Entry<O, Integer> outputEntry : outputMap.entrySet()) {
				totalEncounters += outputEntry.getValue();
			}

			ArrayList<PossibleOutput> outputList = new ArrayList<PossibleOutput>();
			double currentCumulativeProbability = 0.0;

			for (Entry<O, Integer> outputEntry : outputMap.entrySet()) {
				currentCumulativeProbability += outputEntry.getValue() / (double) totalEncounters;
				outputList.add(
					new PossibleOutput(currentCumulativeProbability, outputEntry.getKey())
				);
			}

			Collections.sort(outputList);

			compiledInputMap.put(inputEntry.getKey(), outputList);
		}
	}

	public O getNext(I in)
	{
		if (compiledInputMap == null) {
			return null; //TODO exception?
		}

		ArrayList<PossibleOutput> possibleOutputs = compiledInputMap.get(in);

		if (possibleOutputs == null) {
			return null; //TODO choose random output?
		}

		double r = random.nextDouble();

		for (PossibleOutput p : possibleOutputs) {
			if (r <= p.getCumulativeProbability()) {
				return p.getOutput();
			}
		}

		return null; //TODO exception? should not happen
	}
}
