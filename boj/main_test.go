package main

import (
	"bytes"
	"flag"
	"fmt"
	"io/fs"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"testing"
)

var (
	problem = flag.String("problem", "", "Problem No")
)

func TestMain(m *testing.M) {
	flag.Parse()
	os.Exit(m.Run())
}

func TestProblem(t *testing.T) {
	if *problem == "" {
		t.Skip()
	}

	root := *problem
	inputDir := filepath.Join(root, "inputs")
	outputDir := filepath.Join(root, "outputs")
	solution := filepath.Join(root, "soln"+*problem+".go")

	var inputs []string
	var outputs []string

	_ = filepath.WalkDir(inputDir, func(path string, entry fs.DirEntry, _ error) error {
		if entry.IsDir() {
			return nil
		}
		inputs = append(inputs, path)
		return nil
	})
	_ = filepath.WalkDir(outputDir, func(path string, entry fs.DirEntry, _ error) error {
		if entry.IsDir() {
			return nil
		}
		outputs = append(outputs, path)
		return nil
	})

	for no, input := range inputs {
		t.Run(fmt.Sprintf("TestCase_#%d", no+1), func(t *testing.T) {
			inputFile, _ := os.ReadFile(input)
			outputFile, _ := os.ReadFile(outputs[no])
			var stdout, stderr bytes.Buffer
			cmd := exec.Command("go", "run", solution)
			cmd.Stdin = bytes.NewReader(inputFile)
			cmd.Stdout = &stdout
			cmd.Stderr = &stderr
			_ = cmd.Run()

			res := strings.TrimRight(stdout.String(), "\n")
			exp := strings.TrimRight(string(outputFile), "\n")

			if res != exp {
				t.Logf("\nwrong:\n%s", res)
				t.Logf("\nanswer:\n%s", exp)
				t.Fail()
			}
		})
	}
}
